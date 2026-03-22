

# File alRailRider.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Rail**](dir_7704832a95887b8dfaac4c9470889cbe.md) **>** [**alRailRider.cpp**](al_rail_rider_8cpp.md)

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


