

# Class al::NerveStateBase



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**NerveStateBase**](classal_1_1_nerve_state_base.md)





* `#include <alNerveStateBase.h>`



Inherits the following classes: [al::NerveExecutor](classal_1_1_nerve_executor.md)


Inherited by the following classes: [al::HostStateBase](classal_1_1_host_state_base.md),  [al::ActorStateBase](classal_1_1_actor_state_base.md),  [al::HostStateBase](classal_1_1_host_state_base.md)








































































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**NerveStateBase**](#function-nervestatebase) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**appear**](#function-appear) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**control**](#function-control) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**init**](#function-init) () <br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isDead**](#function-isdead) () const<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**kill**](#function-kill) () <br> |
| virtual [**bool**](classal_1_1_functor_v0_m.md) | [**update**](#function-update) () <br> |


## Public Functions inherited from al::NerveExecutor

See [al::NerveExecutor](classal_1_1_nerve_executor.md)

| Type | Name |
| ---: | :--- |
|   | [**NerveExecutor**](classal_1_1_nerve_executor.md#function-nerveexecutor) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name) <br> |
| virtual [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**getNerveKeeper**](classal_1_1_nerve_executor.md#function-getnervekeeper) () const<br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initNerve**](classal_1_1_nerve_executor.md#function-initnerve) ([**const**](classal_1_1_functor_v0_m.md) [**Nerve**](structal_1_1_nerve.md) \* nrv, [**int**](classal_1_1_functor_v0_m.md) step=0) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**updateNerve**](classal_1_1_nerve_executor.md#function-updatenerve) () <br> |
| virtual  | [**~NerveExecutor**](classal_1_1_nerve_executor.md#function-nerveexecutor) () <br> |


## Public Functions inherited from al::IUseNerve

See [al::IUseNerve](classal_1_1_i_use_nerve.md)

| Type | Name |
| ---: | :--- |
| virtual [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**getNerveKeeper**](classal_1_1_i_use_nerve.md#function-getnervekeeper) () const = 0<br> |
















































































## Public Functions Documentation




### function NerveStateBase 

```C++
al::NerveStateBase::NerveStateBase (
    const  char * name
) 
```




<hr>



### function appear 

```C++
virtual void al::NerveStateBase::appear () 
```




<hr>



### function control 

```C++
virtual void al::NerveStateBase::control () 
```




<hr>



### function init 

```C++
virtual void al::NerveStateBase::init () 
```




<hr>



### function isDead 

```C++
inline bool al::NerveStateBase::isDead () const
```




<hr>



### function kill 

```C++
virtual void al::NerveStateBase::kill () 
```




<hr>



### function update 

```C++
virtual bool al::NerveStateBase::update () 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/include/Nerve/alNerveStateBase.h`

