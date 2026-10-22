#include <Camera/CameraRotatorParam.h>
#include <Yaml/alByamlIter.h>



CameraRotatorParam::CameraRotatorParam() : mAngleMax( 30 )
{
}

void CameraRotatorParam::init( const al::ByamlIter* ticket )
{
        al::ByamlIter h;
        ticket->tryGetIterByKey( &h, "Rotator" );
        h.tryGetFloatByKey( &mAngleMax, "AngleMax" );
}
