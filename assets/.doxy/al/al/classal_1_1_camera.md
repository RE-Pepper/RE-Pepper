

# Class al::Camera



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**Camera**](classal_1_1_camera.md)





* `#include <alCamera.h>`





































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**Camera**](#function-camera) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**calc**](#function-calc) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**load**](#function-load) ([**const**](classal_1_1_functor_v0_m.md) [**ByamlIter**](classal_1_1_byaml_iter.md) \* ticket) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v1**](#function-v1) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v2**](#function-v2) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v3**](#function-v3) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v4**](#function-v4) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v5**](#function-v5) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v7**](#function-v7) () <br> |








## Protected Attributes

| Type | Name |
| ---: | :--- |
|  sead::Vector3f | [**\_2C**](#variable-_2c)  <br> |
|  sead::Vector3f | [**\_8**](#variable-_8)  <br> |
|  [**CameraDashAngleTunerParam**](classal_1_1_camera_dash_angle_tuner_param.md) \* | [**mDashAngleTunerParam**](#variable-mdashangletunerparam)  <br> |
|  [**int**](classal_1_1_functor_v0_m.md) | [**mInterpoleFrame**](#variable-minterpoleframe)  <br> |
|  sead::Vector3f | [**mPos**](#variable-mpos)  <br> |
|  [**CameraRotatorParam**](classal_1_1_camera_rotator_param.md) \* | [**mRotatorParam**](#variable-mrotatorparam)  <br> |
|  sead::Vector3f | [**mTarget**](#variable-mtarget)  <br> |
|  [**CameraUnknownParam**](classal_1_1_camera_unknown_param.md) \* | [**mUnknownParam**](#variable-munknownparam)  <br> |
|  [**CameraParamVision**](classal_1_1_camera_param_vision.md) \* | [**mVisionParam**](#variable-mvisionparam)  <br> |




















## Public Functions Documentation




### function Camera 

```C++
al::Camera::Camera (
    const  char * name
) 
```




<hr>



### function calc 

```C++
virtual void al::Camera::calc () 
```




<hr>



### function load 

```C++
virtual void al::Camera::load (
    const  ByamlIter * ticket
) 
```




<hr>



### function v1 

```C++
virtual void al::Camera::v1 () 
```




<hr>



### function v2 

```C++
virtual void al::Camera::v2 () 
```




<hr>



### function v3 

```C++
virtual void al::Camera::v3 () 
```




<hr>



### function v4 

```C++
virtual void al::Camera::v4 () 
```




<hr>



### function v5 

```C++
virtual void al::Camera::v5 () 
```




<hr>



### function v7 

```C++
virtual void al::Camera::v7 () 
```




<hr>
## Protected Attributes Documentation




### variable \_2C 

```C++
sead::Vector3f al::Camera::_2C;
```




<hr>



### variable \_8 

```C++
sead::Vector3f al::Camera::_8;
```




<hr>



### variable mDashAngleTunerParam 

```C++
CameraDashAngleTunerParam* al::Camera::mDashAngleTunerParam;
```




<hr>



### variable mInterpoleFrame 

```C++
int al::Camera::mInterpoleFrame;
```




<hr>



### variable mPos 

```C++
sead::Vector3f al::Camera::mPos;
```




<hr>



### variable mRotatorParam 

```C++
CameraRotatorParam* al::Camera::mRotatorParam;
```




<hr>



### variable mTarget 

```C++
sead::Vector3f al::Camera::mTarget;
```




<hr>



### variable mUnknownParam 

```C++
CameraUnknownParam* al::Camera::mUnknownParam;
```




<hr>



### variable mVisionParam 

```C++
CameraParamVision* al::Camera::mVisionParam;
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/include/Camera/alCamera.h`

