

# File alRailRider.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Rail**](dir_6ff4c1b13859b82bf8a5d6f47c0db9b6.md) **>** [**alRailRider.cpp**](al_rail_rider_8cpp.md)

[Go to the documentation of this file](al_rail_rider_8cpp.md)


```C++
#include <Math/alMathUtil.h>
#include <Rail/alRail.h>
#include <Rail/alRailRider.h>

namespace al
{

#ifdef NON_MATCHING
// compiler completely skips _4 _10 (????????)
RailRider::RailRider( Rail* rail )
    : mRail( rail ), mCurrentPos( sead::Vector3f::zero ), mCurrentDir( sead::Vector3f::zero ), _1C( 0.0 ),
      mSpeed( 0.0 ), mIsLoop( true )
{
        _1C = mRail->normalizeLength( _1C );
        mRail->calcPosDir( &mCurrentPos, &mCurrentDir, _1C );
}
#endif

void RailRider::moveToRailStart()
{
        _1C = 0.0;
        _1C = mRail->normalizeLength( _1C );
        mRail->calcPosDir( &mCurrentPos, &mCurrentDir, _1C );
}

void RailRider::moveToNearestRail( const sead::Vector3f& r1 )
{
        _1C = mRail->calcNearestRailPosCoord( r1, 20.0f );
        _1C = mRail->normalizeLength( _1C );
        mRail->calcPosDir( &mCurrentPos, &mCurrentDir, _1C );
}

bool RailRider::isReachedGoal() const
{
        if ( !mRail->isClosed() && al::isNearZero( _1C ) )
                return true;
        if ( !mRail->isClosed() && isNearZero( _1C - mRail->getTotalLength() ) )
                return true;

        return false;
}

} // namespace al
```


