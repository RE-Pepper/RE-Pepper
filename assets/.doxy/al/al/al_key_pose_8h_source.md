

# File alKeyPose.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**KeyPose**](dir_c1df91a8d2930eb97f96869b778a7e0b.md) **>** [**alKeyPose.h**](al_key_pose_8h.md)

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


