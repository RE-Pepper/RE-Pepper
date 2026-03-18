

# File alCameraRotatorParam.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Camera**](dir_b39408af9c4561f6cdf388b41f39f7f7.md) **>** [**alCameraRotatorParam.h**](al_camera_rotator_param_8h.md)

[Go to the documentation of this file](al_camera_rotator_param_8h.md)


```C++
#pragma once

namespace al
{

class ByamlIter;

class CameraRotatorParam
{
private:
        float mAngleMax;

public:
        void init( const ByamlIter* ticket );

public:
        CameraRotatorParam();
};

} // namespace al
```


