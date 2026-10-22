#include <Camera/CameraDashAngleTunerParam.h>
#include <Yaml/alByamlIter.h>



CameraDashAngleTunerParam::CameraDashAngleTunerParam() : mAddAngleMax( 15 ), mZoomOutOffsetMax( 200 )
{
}

void CameraDashAngleTunerParam::init( const al::ByamlIter* ticket )
{
        al::ByamlIter h;
        ticket->tryGetIterByKey( &h, "DashAngleTuner" );
        h.tryGetFloatByKey( &mAddAngleMax, "AddAngleMax" );
        h.tryGetFloatByKey( &mZoomOutOffsetMax, "ZoomOutOffsetMax" );
}
