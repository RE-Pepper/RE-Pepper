

# File alRailRider.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Rail**](dir_c8bcdc1e1ae46381fd1d0b5e3e0c3157.md) **>** [**alRailRider.h**](al_rail_rider_8h.md)

[Go to the documentation of this file](al_rail_rider_8h.md)


```C++
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
```


