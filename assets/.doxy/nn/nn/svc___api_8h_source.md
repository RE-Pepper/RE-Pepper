

# File svc\_Api.h

[**File List**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**include**](dir_af9254bf4d22366cfccd04cbaa9622aa.md) **>** [**nn**](dir_a185e92459882a1d3c4a0e5724303e75.md) **>** [**svc**](dir_c1b0279480f3283373e7c3eb28175a75.md) **>** [**svc\_Api.h**](svc___api_8h.md)

[Go to the documentation of this file](svc___api_8h.md)


```C++
#pragma once

#include <nn/Handle.h>
#include <nn/Result.h>
#include <nn/dbg/dbg_Types.h>
#include <nn/os/os_Types.h>

namespace nn {
namespace svc {
    __asm nn::Result ControlMemory(u32* addr, u32 addr0, u32 addr1, u32 size, u32 op, u32 perms);
    __asm void ExitProcess();
    __asm void SleepThread(u64 nanos);
    __asm nn::Result GetThreadPriority(s32* prio, nn::Handle thread);
    __asm nn::Result CreateMutex(nn::Handle* mutex, bool initialLocked);
    __asm nn::Result CreateEvent(nn::Handle* event, nn::os::ResetType type);
    __asm nn::Result CreateMemoryBlock(nn::Handle* memblock, u32 addr, u32 size, u32 myperms, u32 otherperms);
    __asm nn::Result CreateAddressArbiter(nn::Handle* arbiter);
    __asm nn::Result ArbitrateAddress(nn::Handle arbiter, uintptr_t addr, nn::os::ArbitrationType type, s32 value, s64 ns);
    __asm nn::Result CloseHandle(nn::Handle handle);
    __asm nn::Result WaitSynchronizationN(int* out, const nn::Handle* handles, s32 handleCount, bool waitAll, s64 timeout_ns);
    __asm nn::Result DuplicateHandle(nn::Handle* out, nn::Handle original);
    __asm nn::Result ConnectToPort(nn::Handle* port, const char* portName);
    __asm nn::Result GetProcessId(unsigned int* id, nn::Handle handle);
    __asm nn::Result GetThreadId(unsigned int* id, nn::Handle handle);
    __asm nn::Result GetResourceLimit(Handle* resourceLimit, nn::Handle handle);

    // Debug
    __asm nn::Result Break(nn::dbg::BreakReason reason);

} // namespace svc
} // namespace nn
```


