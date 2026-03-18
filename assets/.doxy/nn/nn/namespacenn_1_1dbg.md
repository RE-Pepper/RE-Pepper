

# Namespace nn::dbg



[**Namespace List**](namespaces.md) **>** [**nn**](namespacenn.md) **>** [**dbg**](namespacenn_1_1dbg.md)






















## Public Types

| Type | Name |
| ---: | :--- |
| enum  | [**BreakReason**](#enum-breakreason)  <br> |




















## Public Functions

| Type | Name |
| ---: | :--- |
|  void | [**Break**](#function-break) ([**BreakReason**](namespacenn_1_1dbg.md#enum-breakreason) reason) <br> |




























## Public Types Documentation




### enum BreakReason 

```C++
enum nn::dbg::BreakReason {
    BreakReason_PANIC,
    BreakReason_ASSERT,
    BreakReason_USER,
    BreakReason_LOAD_RO,
    BreakReason_UNLOAD_RO
};
```




<hr>
## Public Functions Documentation




### function Break 

```C++
void nn::dbg::Break (
    BreakReason reason
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `lib/CtrSDK/include/nn/dbg/dbg_Api.h`

