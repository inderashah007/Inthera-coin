#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

// Kernel function untuk mengira ITC berdasarkan data buangan
__global__ void calculateITC(float *usage, float *quota, float *waste, float *itc, int size) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < size) {
        waste[idx] = (usage[idx] < quota[idx]) ? (quota[idx] - usage[idx]) : 0.0f;
        itc[idx] = waste[idx] * 1.0f; // 1 ITC per GB
    }
}

int main() {
    const int dataSize = 10;
    const int threadsPerBlock = 4;
    const int blocksPerGrid = (dataSize + threadsPerBlock - 1) / threadsPerBlock;

    float usage[dataSize], quota[dataSize], waste[dataSize], itc[dataSize];
    float *d_usage, *d_quota, *d_waste, *d_itc;

    srand(time(0));
    for (int i = 0; i < dataSize; i++) {
        usage[i] = static_cast<float>(rand() % 100);
        quota[i] = static_cast<float>((rand() % 50) + 50);
    }

    cudaMalloc((void**)&d_usage, dataSize * sizeof(float));
    cudaMalloc((void**)&d_quota, dataSize * sizeof(float));
    cudaMalloc((void**)&d_waste, dataSize * sizeof(float));
    cudaMalloc((void**)&d_itc, dataSize * sizeof(float));

    cudaMemcpy(d_usage, usage, dataSize * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_quota, quota, dataSize * sizeof(float), cudaMemcpyHostToDevice);

    calculateITC<<<blocksPerGrid, threadsPerBlock>>>(d_usage, d_quota, d_waste, d_itc, dataSize);

    cudaMemcpy(waste, d_waste, dataSize * sizeof(float), cudaMemcpyDeviceToHost);
    cudaMemcpy(itc, d_itc, dataSize * sizeof(float), cudaMemcpyDeviceToHost);

    cout << "User | Usage (GB) | Quota (GB) | Waste (GB) | ITC" << endl;
    for (int i = 0; i < dataSize; i++) {
        cout << i + 1 << " | " << usage[i] << " | " << quota[i] << " | " << waste[i] << " | " << itc[i] << endl;
    }

    cudaFree(d_usage);
    cudaFree(d_quota);
    cudaFree(d_waste);
    cudaFree(d_itc);

    return 0;
}
