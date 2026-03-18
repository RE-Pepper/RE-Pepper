

# Class al::AreaObj



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**AreaObj**](classal_1_1_area_obj.md)





* `#include <alAreaObj.h>`



Inherits the following classes: [al::IUseStageSwitch](classal_1_1_i_use_stage_switch.md)






















































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**AreaObj**](#function-areaobj) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name) <br> |
| virtual [**StageSwitchKeeper**](classal_1_1_stage_switch_keeper.md) \* | [**getStageSwitchKeeper**](#function-getstageswitchkeeper) () const<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**init**](#function-init) ([**const**](classal_1_1_functor_v0_m.md) [**AreaInitInfo**](classal_1_1_area_init_info.md) & info) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**initStageSwitchKeeper**](#function-initstageswitchkeeper) () <br> |
| virtual [**bool**](classal_1_1_functor_v0_m.md) | [**isInVolume**](#function-isinvolume) ([**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & trans) const<br> |


## Public Functions inherited from al::IUseStageSwitch

See [al::IUseStageSwitch](classal_1_1_i_use_stage_switch.md)

| Type | Name |
| ---: | :--- |
| virtual [**StageSwitchKeeper**](classal_1_1_stage_switch_keeper.md) \* | [**getStageSwitchKeeper**](classal_1_1_i_use_stage_switch.md#function-getstageswitchkeeper) () const = 0<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**initStageSwitchKeeper**](classal_1_1_i_use_stage_switch.md#function-initstageswitchkeeper) () = 0<br> |






















































## Public Functions Documentation




### function AreaObj 

```C++
al::AreaObj::AreaObj (
    const  char * name
) 
```




<hr>



### function getStageSwitchKeeper 

```C++
virtual StageSwitchKeeper * al::AreaObj::getStageSwitchKeeper () const
```



Implements [*al::IUseStageSwitch::getStageSwitchKeeper*](classal_1_1_i_use_stage_switch.md#function-getstageswitchkeeper)


<hr>



### function init 

```C++
virtual void al::AreaObj::init (
    const  AreaInitInfo & info
) 
```




<hr>



### function initStageSwitchKeeper 

```C++
virtual void al::AreaObj::initStageSwitchKeeper () 
```



Implements [*al::IUseStageSwitch::initStageSwitchKeeper*](classal_1_1_i_use_stage_switch.md#function-initstageswitchkeeper)


<hr>



### function isInVolume 

```C++
virtual bool al::AreaObj::isInVolume (
    const sead::Vector3f & trans
) const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/include/AreaObj/alAreaObj.h`

