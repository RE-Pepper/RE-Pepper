

# File CameraFollow.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Camera**](dir_4cdbb219ebc4b6f005e00b0a493e52da.md) **>** [**CameraFollow.h**](_camera_follow_8h.md)

[Go to the documentation of this file](_camera_follow_8h.md)


```C++
#pragma once

#include <Camera/alCamera.h>

class CameraFollow : public al::Camera
{
private:
        void* _4C;
        float _50;
        float _54;
        float _58;
        float _5C;
        float _60;
        float _64;
        float _68;
        float _6C;
        float _70;
        float _74;
        float _78;

public:
        virtual void load( const al::ByamlIter* ticket );
        virtual void calc();

public:
        CameraFollow( const char* name );
};
```


