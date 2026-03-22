

# File alKeyPose.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**KeyPose**](dir_685f8e5aad470601699f790a00ee6ee2.md) **>** [**alKeyPose.cpp**](al_key_pose_8cpp.md)

[Go to the documentation of this file](al_key_pose_8cpp.md)


```C++
#pragma once

#include <KeyPose/alKeyPose.h>
#include <Placement/alPlacementFunction.h>

namespace al
{

KeyPose::KeyPose()
    : mQuat( sead::Quatf::unit ), mTrans( sead::Vector3f::zero ), mPlacementInfo( nullptr ), _20( 0.0 )
{
}

void KeyPose::init( const PlacementInfo& info )
{
        tryGetQuat( &mQuat, info );
        tryGetTrans( &mTrans, info );
        mPlacementInfo = new PlacementInfo( info );
}

} // namespace al
```


