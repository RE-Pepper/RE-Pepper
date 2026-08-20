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
