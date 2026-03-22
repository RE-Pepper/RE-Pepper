

# File CameraAnim.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Camera**](dir_4cdbb219ebc4b6f005e00b0a493e52da.md) **>** [**CameraAnim.h**](_camera_anim_8h.md)

[Go to the documentation of this file](_camera_anim_8h.md)


```C++
#pragma once

#include <Camera/alCamera.h>

class CameraAnim : public al::Camera
{
private:
        int _4C;
        int _50;
        int _54;
        int _58;

public:
        virtual void load( const al::ByamlIter* ticket );
        virtual void calc();

public:
        CameraAnim( const char* name );
};
```


