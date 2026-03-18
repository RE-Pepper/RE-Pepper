

# Class al::AsyncFunctorThread



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**AsyncFunctorThread**](classal_1_1_async_functor_thread.md)





* `#include <alAsyncFunctorThread.h>`





































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**AsyncFunctorThread**](#function-asyncfunctorthread) ([**const**](classal_1_1_functor_v0_m.md) sead::SafeString & name, [**const**](classal_1_1_functor_v0_m.md) [**FunctorBase**](classal_1_1_functor_base.md) & functor, [**int**](classal_1_1_functor_v0_m.md)) <br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isDone**](#function-isdone) () const<br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**start**](#function-start) () <br> |
| virtual  | [**~AsyncFunctorThread**](#function-asyncfunctorthread) () <br> |




























## Public Functions Documentation




### function AsyncFunctorThread 

```C++
al::AsyncFunctorThread::AsyncFunctorThread (
    const sead::SafeString & name,
    const  FunctorBase & functor,
    int
) 
```




<hr>



### function isDone 

```C++
inline bool al::AsyncFunctorThread::isDone () const
```




<hr>



### function start 

```C++
void al::AsyncFunctorThread::start () 
```




<hr>



### function ~AsyncFunctorThread 

```C++
virtual al::AsyncFunctorThread::~AsyncFunctorThread () 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/include/System/alAsyncFunctorThread.h`

