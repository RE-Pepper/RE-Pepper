

# File alKeyPose.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**KeyPose**](dir_bf1c47771fd9df1cf199e26225c12bef.md) **>** [**alKeyPose.cpp**](al_key_pose_8cpp.md)

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


