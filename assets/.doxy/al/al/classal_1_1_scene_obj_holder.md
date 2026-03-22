

# Class al::SceneObjHolder



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**SceneObjHolder**](classal_1_1_scene_obj_holder.md)





* `#include <alSceneObjHolder.h>`





































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**SceneObjHolder**](#function-sceneobjholder) ([**CreateFunc**](classal_1_1_scene_obj_holder.md#typedef-createfunc) func, [**int**](classal_1_1_functor_v0_m.md) size) <br> |
|  [**ISceneObj**](classal_1_1_i_scene_obj.md) \* | [**create**](#function-create) ([**int**](classal_1_1_functor_v0_m.md) id) <br> |
|  [**ISceneObj**](classal_1_1_i_scene_obj.md) \* | [**getObj**](#function-getobj) ([**int**](classal_1_1_functor_v0_m.md) id) const<br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initAfterPlacementSceneObj**](#function-initafterplacementsceneobj) ([**const**](classal_1_1_functor_v0_m.md) [**ActorInitInfo**](classal_1_1_actor_init_info.md) & info) <br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isExist**](#function-isexist) ([**int**](classal_1_1_functor_v0_m.md) id) const<br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**setObj**](#function-setobj) ([**ISceneObj**](classal_1_1_i_scene_obj.md) \* obj, [**int**](classal_1_1_functor_v0_m.md) id) <br> |




























## Public Functions Documentation




### function SceneObjHolder 

```C++
al::SceneObjHolder::SceneObjHolder (
    CreateFunc func,
    int size
) 
```




<hr>



### function create 

```C++
ISceneObj * al::SceneObjHolder::create (
    int id
) 
```




<hr>



### function getObj 

```C++
ISceneObj * al::SceneObjHolder::getObj (
    int id
) const
```




<hr>



### function initAfterPlacementSceneObj 

```C++
void al::SceneObjHolder::initAfterPlacementSceneObj (
    const  ActorInitInfo & info
) 
```




<hr>



### function isExist 

```C++
bool al::SceneObjHolder::isExist (
    int id
) const
```




<hr>



### function setObj 

```C++
void al::SceneObjHolder::setObj (
    ISceneObj * obj,
    int id
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/Scene/alSceneObjHolder.h`

