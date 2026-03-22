#pragma once

#include <math/seadVector.h>

namespace al
{
class Rail;

class RailRider
{
private:
        Rail*          mRail;
        sead::Vector3f mCurrentPos;
        sead::Vector3f mCurrentDir;
        float          _1C;
        float          mSpeed;
        bool           mIsLoop;

public:
        void moveToRailStart();
        void moveToNearestRail( const sead::Vector3f& r1 );

        bool isReachedGoal() const;

        void setSpeed( float speed )
        {
                mSpeed = speed;
        }

        const sead::Vector3f& getCurrentPos() const
        {
                return mCurrentPos;
        }

        const sead::Vector3f& getCurrentDir() const
        {
                return mCurrentDir;
        }

        bool isLoop() const
        {
                return mIsLoop;
        }

public:
        RailRider( Rail* rail );
};

} // namespace al
