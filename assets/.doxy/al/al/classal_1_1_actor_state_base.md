

# Class al::ActorStateBase



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**ActorStateBase**](classal_1_1_actor_state_base.md)





* `#include <alActorStateBase.h>`



Inherits the following classes: [al::NerveStateBase](classal_1_1_nerve_state_base.md)






























































































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**ActorStateBase**](#function-actorstatebase) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name, [**LiveActor**](classal_1_1_live_actor.md) \* host) <br> |


## Public Functions inherited from al::NerveStateBase

See [al::NerveStateBase](classal_1_1_nerve_state_base.md)

| Type | Name |
| ---: | :--- |
|   | [**NerveStateBase**](classal_1_1_nerve_state_base.md#function-nervestatebase) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**appear**](classal_1_1_nerve_state_base.md#function-appear) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**control**](classal_1_1_nerve_state_base.md#function-control) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**init**](classal_1_1_nerve_state_base.md#function-init) () <br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isDead**](classal_1_1_nerve_state_base.md#function-isdead) () const<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**kill**](classal_1_1_nerve_state_base.md#function-kill) () <br> |
| virtual [**bool**](classal_1_1_functor_v0_m.md) | [**update**](classal_1_1_nerve_state_base.md#function-update) () <br> |


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


























## Protected Attributes

| Type | Name |
| ---: | :--- |
|  [**LiveActor**](classal_1_1_live_actor.md) \*[**const**](classal_1_1_functor_v0_m.md) | [**mHost**](#variable-mhost)  <br> |
















































































## Public Functions Documentation




### function ActorStateBase 

```C++
inline al::ActorStateBase::ActorStateBase (
    const  char * name,
    LiveActor * host
) 
```




<hr>
## Protected Attributes Documentation




### variable mHost 

```C++
LiveActor* const al::ActorStateBase::mHost;
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/include/Nerve/alActorStateBase.h`

