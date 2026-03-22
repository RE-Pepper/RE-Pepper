

# File PlayerProperty.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**PlayerProperty.h**](_player_property_8h.md)

[Go to the documentation of this file](_player_property_8h.md)


```C++
#pragma once

#include <math/seadVector.h>

class PlayerProperty
{
private:
        sead::Vector3f mTrans;
        sead::Vector3f mFront;
        sead::Vector3f mUp;
        u8             _C[ 0x54 ];

public:
        void setFrontVec( const sead::Vector3f& front );
        void setUpVec( const sead::Vector3f& up );
};
```


