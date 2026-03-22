

# Class al::LiveActorGroup



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**LiveActorGroup**](classal_1_1_live_actor_group.md)





* `#include <alLiveActorGroup.h>`





































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**LiveActorGroup**](#function-liveactorgroup) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name, [**int**](classal_1_1_functor_v0_m.md) bufSize) <br> |
|  sead::PtrArray&lt; [**T**](classal_1_1_functor_v0_m.md) &gt; & | [**getArray**](#function-getarray) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**killAll**](#function-killall) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**makeActorDeadAll**](#function-makeactordeadall) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**registerActor**](#function-registeractor) ([**LiveActor**](classal_1_1_live_actor.md) \* actor) <br> |




























## Public Functions Documentation




### function LiveActorGroup 

```C++
al::LiveActorGroup::LiveActorGroup (
    const  char * name,
    int bufSize
) 
```




<hr>



### function getArray 

```C++
template<typename  T>
inline sead::PtrArray< T > & al::LiveActorGroup::getArray () 
```




<hr>



### function killAll 

```C++
void al::LiveActorGroup::killAll () 
```




<hr>



### function makeActorDeadAll 

```C++
void al::LiveActorGroup::makeActorDeadAll () 
```




<hr>



### function registerActor 

```C++
virtual void al::LiveActorGroup::registerActor (
    LiveActor * actor
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/LiveActor/alLiveActorGroup.h`

