

# Namespace nn::svc



[**Namespace List**](namespaces.md) **>** [**nn**](namespacenn.md) **>** [**svc**](namespacenn_1_1svc.md)


























## Public Attributes

| Type | Name |
| ---: | :--- |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) [**u32**](types_8h.md#typedef-u32) | [**addr0**](#variable-addr0)  <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) [**u32**](types_8h.md#typedef-u32) [**u32**](types_8h.md#typedef-u32) | [**addr1**](#variable-addr1)  <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) [**u32**](types_8h.md#typedef-u32) [**u32**](types_8h.md#typedef-u32) [**u32**](types_8h.md#typedef-u32) [**u32**](types_8h.md#typedef-u32) | [**op**](#variable-op)  <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) [**u32**](types_8h.md#typedef-u32) [**u32**](types_8h.md#typedef-u32) [**u32**](types_8h.md#typedef-u32) | [**size**](#variable-size)  <br> |
















## Public Functions

| Type | Name |
| ---: | :--- |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**ArbitrateAddress**](#function-arbitrateaddress) ([**nn::Handle**](structnn_1_1_handle.md) arbiter, [**uintptr\_t**](types_8h.md#typedef-uintptr_t) addr, [**nn::os::ArbitrationType**](namespacenn_1_1os.md#enum-arbitrationtype) type, [**s32**](types_8h.md#typedef-s32) value, [**s64**](types_8h.md#typedef-s64) ns) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**Break**](#function-break) ([**nn::dbg::BreakReason**](namespacenn_1_1dbg.md#enum-breakreason) reason) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**CloseHandle**](#function-closehandle) ([**nn::Handle**](structnn_1_1_handle.md) handle) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**ConnectToPort**](#function-connecttoport) ([**nn::Handle**](structnn_1_1_handle.md) \* port, const char \* portName) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**ControlMemory**](#function-controlmemory) ([**u32**](types_8h.md#typedef-u32) \* addr, [**u32**](types_8h.md#typedef-u32) addr0, [**u32**](types_8h.md#typedef-u32) addr1, [**u32**](types_8h.md#typedef-u32) size, [**u32**](types_8h.md#typedef-u32) op, [**u32**](types_8h.md#typedef-u32) perms) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**CreateAddressArbiter**](#function-createaddressarbiter) ([**nn::Handle**](structnn_1_1_handle.md) \* arbiter) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**CreateEvent**](#function-createevent) ([**nn::Handle**](structnn_1_1_handle.md) \* event, [**nn::os::ResetType**](namespacenn_1_1os.md#enum-resettype) type) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**CreateMemoryBlock**](#function-creatememoryblock) ([**nn::Handle**](structnn_1_1_handle.md) \* memblock, [**u32**](types_8h.md#typedef-u32) addr, [**u32**](types_8h.md#typedef-u32) size, [**u32**](types_8h.md#typedef-u32) myperms, [**u32**](types_8h.md#typedef-u32) otherperms) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**CreateMutex**](#function-createmutex) ([**nn::Handle**](structnn_1_1_handle.md) \* mutex, bool initialLocked) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**DuplicateHandle**](#function-duplicatehandle) ([**nn::Handle**](structnn_1_1_handle.md) \* out, [**nn::Handle**](structnn_1_1_handle.md) original) <br> |
|  \_\_asm void | [**ExitProcess**](#function-exitprocess) () <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**GetProcessId**](#function-getprocessid) (unsigned int \* id, [**nn::Handle**](structnn_1_1_handle.md) handle) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**GetResourceLimit**](#function-getresourcelimit) ([**Handle**](structnn_1_1_handle.md) \* resourceLimit, [**nn::Handle**](structnn_1_1_handle.md) handle) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**GetThreadId**](#function-getthreadid) (unsigned int \* id, [**nn::Handle**](structnn_1_1_handle.md) handle) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**GetThreadPriority**](#function-getthreadpriority) ([**s32**](types_8h.md#typedef-s32) \* prio, [**nn::Handle**](structnn_1_1_handle.md) thread) <br> |
|  \_\_asm void | [**SleepThread**](#function-sleepthread) ([**u64**](types_8h.md#typedef-u64) nanos) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**WaitSynchronizationN**](#function-waitsynchronizationn) (int \* out, const [**nn::Handle**](structnn_1_1_handle.md) \* handles, [**s32**](types_8h.md#typedef-s32) handleCount, bool waitAll, [**s64**](types_8h.md#typedef-s64) timeout\_ns) <br> |
|  \_\_asm [**nn::Result**](classnn_1_1_result.md) | [**\_\_attribute\_\_**](#function-__attribute__) ((section("i.\_ZN2nn3svc13ControlMemoryEPjjjjjj"))) <br> |




























## Public Attributes Documentation




### variable addr0 

```C++
__asm nn::Result u32 nn::svc::addr0;
```




<hr>



### variable addr1 

```C++
__asm nn::Result u32 u32 nn::svc::addr1;
```




<hr>



### variable op 

```C++
__asm nn::Result u32 u32 u32 u32 nn::svc::op;
```




<hr>



### variable size 

```C++
__asm nn::Result u32 u32 u32 nn::svc::size;
```




<hr>
## Public Functions Documentation




### function ArbitrateAddress 

```C++
__asm nn::Result nn::svc::ArbitrateAddress (
    nn::Handle arbiter,
    uintptr_t addr,
    nn::os::ArbitrationType type,
    s32 value,
    s64 ns
) 
```




<hr>



### function Break 

```C++
__asm nn::Result nn::svc::Break (
    nn::dbg::BreakReason reason
) 
```




<hr>



### function CloseHandle 

```C++
__asm nn::Result nn::svc::CloseHandle (
    nn::Handle handle
) 
```




<hr>



### function ConnectToPort 

```C++
__asm nn::Result nn::svc::ConnectToPort (
    nn::Handle * port,
    const char * portName
) 
```




<hr>



### function ControlMemory 

```C++
__asm nn::Result nn::svc::ControlMemory (
    u32 * addr,
    u32 addr0,
    u32 addr1,
    u32 size,
    u32 op,
    u32 perms
) 
```




<hr>



### function CreateAddressArbiter 

```C++
__asm nn::Result nn::svc::CreateAddressArbiter (
    nn::Handle * arbiter
) 
```




<hr>



### function CreateEvent 

```C++
__asm nn::Result nn::svc::CreateEvent (
    nn::Handle * event,
    nn::os::ResetType type
) 
```




<hr>



### function CreateMemoryBlock 

```C++
__asm nn::Result nn::svc::CreateMemoryBlock (
    nn::Handle * memblock,
    u32 addr,
    u32 size,
    u32 myperms,
    u32 otherperms
) 
```




<hr>



### function CreateMutex 

```C++
__asm nn::Result nn::svc::CreateMutex (
    nn::Handle * mutex,
    bool initialLocked
) 
```




<hr>



### function DuplicateHandle 

```C++
__asm nn::Result nn::svc::DuplicateHandle (
    nn::Handle * out,
    nn::Handle original
) 
```




<hr>



### function ExitProcess 

```C++
__asm void nn::svc::ExitProcess () 
```




<hr>



### function GetProcessId 

```C++
__asm nn::Result nn::svc::GetProcessId (
    unsigned int * id,
    nn::Handle handle
) 
```




<hr>



### function GetResourceLimit 

```C++
__asm nn::Result nn::svc::GetResourceLimit (
    Handle * resourceLimit,
    nn::Handle handle
) 
```




<hr>



### function GetThreadId 

```C++
__asm nn::Result nn::svc::GetThreadId (
    unsigned int * id,
    nn::Handle handle
) 
```




<hr>



### function GetThreadPriority 

```C++
__asm nn::Result nn::svc::GetThreadPriority (
    s32 * prio,
    nn::Handle thread
) 
```




<hr>



### function SleepThread 

```C++
__asm void nn::svc::SleepThread (
    u64 nanos
) 
```




<hr>



### function WaitSynchronizationN 

```C++
__asm nn::Result nn::svc::WaitSynchronizationN (
    int * out,
    const nn::Handle * handles,
    s32 handleCount,
    bool waitAll,
    s64 timeout_ns
) 
```




<hr>



### function \_\_attribute\_\_ 

```C++
__asm nn::Result nn::svc::__attribute__ (
    (section("i._ZN2nn3svc13ControlMemoryEPjjjjjj"))
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `lib/CtrSDK/include/nn/svc/svc_Api.h`

