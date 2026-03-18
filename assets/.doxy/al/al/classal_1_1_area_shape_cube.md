

# Class al::AreaShapeCube



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**AreaShapeCube**](classal_1_1_area_shape_cube.md)





* `#include <alAreaShapeCube.h>`



Inherits the following classes: [al::AreaShape](classal_1_1_area_shape.md)






















































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**AreaShapeCube**](#function-areashapecube) ([**bool**](classal_1_1_functor_v0_m.md) isCubeBase) <br> |
| virtual [**bool**](classal_1_1_functor_v0_m.md) | [**isInVolume**](#function-isinvolume) ([**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & trans) const<br> |


## Public Functions inherited from al::AreaShape

See [al::AreaShape](classal_1_1_area_shape.md)

| Type | Name |
| ---: | :--- |
|   | [**AreaShape**](classal_1_1_area_shape.md#function-areashape) () <br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**calcLocalPos**](classal_1_1_area_shape.md#function-calclocalpos) (sead::Vector3f \* out, [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & trans) const<br> |
| virtual [**bool**](classal_1_1_functor_v0_m.md) | [**isInVolume**](classal_1_1_area_shape.md#function-isinvolume) ([**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & trans) const = 0<br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**setBaseMtxPtr**](classal_1_1_area_shape.md#function-setbasemtxptr) ([**const**](classal_1_1_functor_v0_m.md) sead::Matrix34f \* baseMtxPtr) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**setScale**](classal_1_1_area_shape.md#function-setscale) ([**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & scale) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v1**](classal_1_1_area_shape.md#function-v1) () = 0<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v2**](classal_1_1_area_shape.md#function-v2) () = 0<br> |






















































## Public Functions Documentation




### function AreaShapeCube 

```C++
al::AreaShapeCube::AreaShapeCube (
    bool isCubeBase
) 
```




<hr>



### function isInVolume 

```C++
virtual bool al::AreaShapeCube::isInVolume (
    const sead::Vector3f & trans
) const
```



Implements [*al::AreaShape::isInVolume*](classal_1_1_area_shape.md#function-isinvolume)


<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/include/AreaObj/alAreaShapeCube.h`

