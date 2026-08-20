#include <Placement/alPlacementFunction.h>
#include <Rail/alRail.h>
#include <Rail/alRailKeeper.h>
#include <Rail/alRailRider.h>

namespace al
{

RailKeeper::RailKeeper( const PlacementInfo& info ) : mRail( nullptr ), mRailRider( nullptr )
{
        mRail = new Rail;
        mRail->init( info );
        mRailRider = new RailRider( mRail );
}

RailKeeper* tryCreateRailKeeper( const PlacementInfo& info )
{
        PlacementInfo railIter;
        if ( tryGetRailIter( &railIter, info ) )
                return new RailKeeper( railIter );
        return nullptr;
}

bool RailKeeper::isExistRail() const
{
        return mRail != nullptr;
}

} // namespace al
