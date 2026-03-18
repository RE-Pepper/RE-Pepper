

# File types.h



[**FileList**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**include**](dir_af9254bf4d22366cfccd04cbaa9622aa.md) **>** [**nn**](dir_a185e92459882a1d3c4a0e5724303e75.md) **>** [**types.h**](types_8h.md)

[Go to the source code of this file](types_8h_source.md)



* `#include <stdint.h>`
* `#include <stddef.h>`
* `#include <stdarg.h>`

















## Public Types

| Type | Name |
| ---: | :--- |
| typedef float | [**f32**](#typedef-f32)  <br> |
| typedef double | [**f64**](#typedef-f64)  <br> |
| typedef [**s32**](types_8h.md#typedef-s32) | [**intptr\_t**](#typedef-intptr_t)  <br> |
| typedef signed short | [**s16**](#typedef-s16)  <br> |
| typedef signed int | [**s32**](#typedef-s32)  <br> |
| typedef signed long long | [**s64**](#typedef-s64)  <br> |
| typedef signed char | [**s8**](#typedef-s8)  <br> |
| typedef unsigned short | [**u16**](#typedef-u16)  <br> |
| typedef unsigned int | [**u32**](#typedef-u32)  <br> |
| typedef unsigned long long | [**u64**](#typedef-u64)  <br> |
| typedef unsigned char | [**u8**](#typedef-u8)  <br> |
| typedef [**u32**](types_8h.md#typedef-u32) | [**uintptr\_t**](#typedef-uintptr_t)  <br> |















































## Macros

| Type | Name |
| ---: | :--- |
| define  | [**NULL**](types_8h.md#define-null)  `(void\*)0`<br> |
| define  | [**nullptr**](types_8h.md#define-nullptr)  `[**NULL**](types_8h.md#define-null)`<br> |
| define  | [**split**](types_8h.md#define-split) (S) `\_\_attribute\_\_( ( section( ".sdata\_" #S ) ) ) S`<br> |

## Public Types Documentation




### typedef f32 

```C++
typedef float f32;
```




<hr>



### typedef f64 

```C++
typedef double f64;
```




<hr>



### typedef intptr\_t 

```C++
typedef s32 intptr_t;
```




<hr>



### typedef s16 

```C++
typedef signed short s16;
```




<hr>



### typedef s32 

```C++
typedef signed int s32;
```




<hr>



### typedef s64 

```C++
typedef signed long long s64;
```




<hr>



### typedef s8 

```C++
typedef signed char s8;
```




<hr>



### typedef u16 

```C++
typedef unsigned short u16;
```




<hr>



### typedef u32 

```C++
typedef unsigned int u32;
```




<hr>



### typedef u64 

```C++
typedef unsigned long long u64;
```




<hr>



### typedef u8 

```C++
typedef unsigned char u8;
```




<hr>



### typedef uintptr\_t 

```C++
typedef u32 uintptr_t;
```




<hr>
## Macro Definition Documentation





### define NULL 

```C++
#define NULL `(void*)0`
```




<hr>



### define nullptr 

```C++
#define nullptr `NULL`
```




<hr>



### define split 

```C++
#define split (
    S
) `__attribute__( ( section( ".sdata_" #S ) ) ) S`
```




<hr>

------------------------------
The documentation for this class was generated from the following file `lib/CtrSDK/include/nn/types.h`

