

# Class al::ISceneObj



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**ISceneObj**](classal_1_1_i_scene_obj.md)





* `#include <alISceneObj.h>`





Inherited by the following classes: [al::CameraDirector](classal_1_1_camera_director.md),  [al::SwitchAreaDirector](classal_1_1_switch_area_director.md)
































## Public Functions

| Type | Name |
| ---: | :--- |
| virtual [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* | [**getSceneObjName**](#function-getsceneobjname) () const = 0<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**initAfterPlacementSceneObj**](#function-initafterplacementsceneobj) ([**const**](classal_1_1_functor_v0_m.md) [**ActorInitInfo**](classal_1_1_actor_init_info.md) & info) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**initSceneObj**](#function-initsceneobj) () <br> |




























## Public Functions Documentation




### function getSceneObjName 

```C++
virtual const  char * al::ISceneObj::getSceneObjName () const = 0
```




<hr>



### function initAfterPlacementSceneObj 

```C++
inline virtual void al::ISceneObj::initAfterPlacementSceneObj (
    const  ActorInitInfo & info
) 
```




<hr>



### function initSceneObj 

```C++
inline virtual void al::ISceneObj::initSceneObj () 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/Scene/alISceneObj.h`

