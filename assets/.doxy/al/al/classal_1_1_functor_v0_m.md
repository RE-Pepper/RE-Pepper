

# Class al::FunctorV0M

**template &lt;[**typename**](classal_1_1_functor_v0_m.md) [**T**](classal_1_1_functor_v0_m.md), [**typename**](classal_1_1_functor_v0_m.md) [**F**](classal_1_1_functor_v0_m.md)&gt;**



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**FunctorV0M**](classal_1_1_functor_v0_m.md)





* `#include <alFunctorV0M.h>`



Inherits the following classes: [al::FunctorBase](classal_1_1_functor_base.md)






















































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**FunctorV0M**](#function-functorv0m) ([**T**](classal_1_1_functor_v0_m.md) parent, [**F**](classal_1_1_functor_v0_m.md) funcPtr) <br> |
| virtual [**FunctorV0M**](classal_1_1_functor_v0_m.md) \* | [**clone**](#function-clone) () const<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**operator()**](#function-operator) () const<br> |


## Public Functions inherited from al::FunctorBase

See [al::FunctorBase](classal_1_1_functor_base.md)

| Type | Name |
| ---: | :--- |
| virtual [**FunctorBase**](classal_1_1_functor_base.md) \* | [**clone**](classal_1_1_functor_base.md#function-clone) () const = 0<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**operator()**](classal_1_1_functor_base.md#function-operator) () const = 0<br> |






















































## Public Functions Documentation




### function FunctorV0M 

```C++
inline al::FunctorV0M::FunctorV0M (
    T parent,
    F funcPtr
) 
```




<hr>



### function clone 

```C++
inline virtual FunctorV0M * al::FunctorV0M::clone () const
```



Implements [*al::FunctorBase::clone*](classal_1_1_functor_base.md#function-clone)


<hr>



### function operator() 

```C++
inline virtual void al::FunctorV0M::operator() () const
```



Implements [*al::FunctorBase::operator()*](classal_1_1_functor_base.md#function-operator)


<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/Functor/alFunctorV0M.h`

