

# File alKeyPose.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**KeyPose**](dir_09c78ece3f2f1ae80a9e8a5794be62d2.md) **>** [**alKeyPose.h**](al_key_pose_8h.md)

[Go to the documentation of this file](al_key_pose_8h.md)


```C++
#pragma once

#include <Placement/alPlacementInfo.h>
#include <math/seadQuat.h>
#include <math/seadVector.h>

namespace al
{

class KeyPose
{
private:
        sead::Quatf          mQuat;
        sead::Vector3f       mTrans;
        const PlacementInfo* mPlacementInfo;
        float                _20;

public:
        void init( const PlacementInfo& info );

        const sead::Quatf& getQuat() const
        {
                return mQuat;
        }

        const sead::Vector3f& getTrans() const
        {
                return mTrans;
        }

        const PlacementInfo* getPlacementInfo() const
        {
                return mPlacementInfo;
        }

public:
        KeyPose();
};

} // namespace al
```


