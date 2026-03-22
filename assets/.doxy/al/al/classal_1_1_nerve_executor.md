

# Class al::NerveExecutor



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**NerveExecutor**](classal_1_1_nerve_executor.md)





* `#include <alNerveExecutor.h>`



Inherits the following classes: [al::IUseNerve](classal_1_1_i_use_nerve.md)


Inherited by the following classes: [al::NerveStateBase](classal_1_1_nerve_state_base.md),  [al::Scene](classal_1_1_scene.md),  [al::Sequence](classal_1_1_sequence.md)




















































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**NerveExecutor**](#function-nerveexecutor) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name) <br> |
| virtual [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**getNerveKeeper**](#function-getnervekeeper) () const<br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initNerve**](#function-initnerve) ([**const**](classal_1_1_functor_v0_m.md) [**Nerve**](structal_1_1_nerve.md) \* nrv, [**int**](classal_1_1_functor_v0_m.md) step=0) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**updateNerve**](#function-updatenerve) () <br> |
| virtual  | [**~NerveExecutor**](#function-nerveexecutor) () <br> |


## Public Functions inherited from al::IUseNerve

See [al::IUseNerve](classal_1_1_i_use_nerve.md)

| Type | Name |
| ---: | :--- |
| virtual [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**getNerveKeeper**](classal_1_1_i_use_nerve.md#function-getnervekeeper) () const = 0<br> |






















































## Public Functions Documentation




### function NerveExecutor 

```C++
al::NerveExecutor::NerveExecutor (
    const  char * name
) 
```




<hr>



### function getNerveKeeper 

```C++
virtual NerveKeeper * al::NerveExecutor::getNerveKeeper () const
```



Implements [*al::IUseNerve::getNerveKeeper*](classal_1_1_i_use_nerve.md#function-getnervekeeper)


<hr>



### function initNerve 

```C++
void al::NerveExecutor::initNerve (
    const  Nerve * nrv,
    int step=0
) 
```




<hr>



### function updateNerve 

```C++
void al::NerveExecutor::updateNerve () 
```




<hr>



### function ~NerveExecutor 

```C++
inline virtual al::NerveExecutor::~NerveExecutor () 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/Nerve/alNerveExecutor.h`

