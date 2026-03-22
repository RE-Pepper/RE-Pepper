

# Class al::ActorInitInfo



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**ActorInitInfo**](classal_1_1_actor_init_info.md)





* `#include <alActorInitInfo.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**void**](classal_1_1_functor_v0_m.md) \* | [**\_10**](#variable-_10)  <br> |
|  [**void**](classal_1_1_functor_v0_m.md) \* | [**\_4**](#variable-_4)  <br> |
|  [**void**](classal_1_1_functor_v0_m.md) \* | [**\_8**](#variable-_8)  <br> |
|  [**void**](classal_1_1_functor_v0_m.md) \* | [**\_C**](#variable-_c)  <br> |
|  [**const**](classal_1_1_functor_v0_m.md) [**PlacementInfo**](namespaceal.md#typedef-placementinfo) \* | [**mPlacementInfo**](#variable-mplacementinfo)  <br> |
|  [**int**](classal_1_1_functor_v0_m.md) | [**mViewId**](#variable-mviewid)  <br> |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**ActorInitInfo**](#function-actorinitinfo) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initNew**](#function-initnew) ([**const**](classal_1_1_functor_v0_m.md) [**PlacementInfo**](namespaceal.md#typedef-placementinfo) \* placement, [**const**](classal_1_1_functor_v0_m.md) [**ActorInitInfo**](classal_1_1_actor_init_info.md) & baseInfo) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initViewIdHost**](#function-initviewidhost) ([**const**](classal_1_1_functor_v0_m.md) [**PlacementInfo**](namespaceal.md#typedef-placementinfo) \* placement, [**const**](classal_1_1_functor_v0_m.md) [**ActorInitInfo**](classal_1_1_actor_init_info.md) & hostInfo) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initViewIdSelf**](#function-initviewidself) ([**const**](classal_1_1_functor_v0_m.md) [**PlacementInfo**](namespaceal.md#typedef-placementinfo) \* placement, [**const**](classal_1_1_functor_v0_m.md) [**ActorInitInfo**](classal_1_1_actor_init_info.md) & hostInfo) <br> |




























## Public Attributes Documentation




### variable \_10 

```C++
void* al::ActorInitInfo::_10;
```




<hr>



### variable \_4 

```C++
void* al::ActorInitInfo::_4;
```




<hr>



### variable \_8 

```C++
void* al::ActorInitInfo::_8;
```




<hr>



### variable \_C 

```C++
void* al::ActorInitInfo::_C;
```




<hr>



### variable mPlacementInfo 

```C++
const PlacementInfo* al::ActorInitInfo::mPlacementInfo;
```




<hr>



### variable mViewId 

```C++
int al::ActorInitInfo::mViewId;
```




<hr>
## Public Functions Documentation




### function ActorInitInfo 

```C++
al::ActorInitInfo::ActorInitInfo () 
```




<hr>



### function initNew 

```C++
void al::ActorInitInfo::initNew (
    const  PlacementInfo * placement,
    const  ActorInitInfo & baseInfo
) 
```




<hr>



### function initViewIdHost 

```C++
void al::ActorInitInfo::initViewIdHost (
    const  PlacementInfo * placement,
    const  ActorInitInfo & hostInfo
) 
```




<hr>



### function initViewIdSelf 

```C++
void al::ActorInitInfo::initViewIdSelf (
    const  PlacementInfo * placement,
    const  ActorInitInfo & hostInfo
) 
```




<hr>## Friends Documentation





### friend getPlacementInfo 

```C++
const  PlacementInfo & al::ActorInitInfo::getPlacementInfo (
    const  ActorInitInfo & info
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/LiveActor/alActorInitInfo.h`

