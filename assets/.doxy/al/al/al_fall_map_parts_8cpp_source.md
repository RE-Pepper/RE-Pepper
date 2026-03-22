

# File alFallMapParts.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**MapObj**](dir_f3f5216313c303753d4964996d78ec44.md) **>** [**alFallMapParts.cpp**](al_fall_map_parts_8cpp.md)

[Go to the documentation of this file](al_fall_map_parts_8cpp.md)


```C++
#include <LiveActor/alActorInitInfo.h>
#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alActorPoseKeeper.h>
#include <LiveActor/alLiveActorFunction.h>
#include <LiveActor/alSensorMsg.h>
#include <MapObj/alFallMapParts.h>
#include <Nerve/alNerve.h>
#include <Nerve/alNerveFunction.h>
#include <Nerve/alNerveKeeper.h>
#include <Placement/alPlacementFunction.h>

namespace al
{

namespace NrvFallMapParts
{

NERVE_DEF( FallMapParts, Appear );
NERVE_DEF( FallMapParts, Wait );
NERVE_DEF( FallMapParts, FallSign );
NERVE_DEF( FallMapParts, Fall );
NERVE_DEF( FallMapParts, End );

} // namespace NrvFallMapParts

#ifdef NON_MATCHING
// float
FallMapParts::FallMapParts( const sead::SafeString& name )
    : MapObjActor( name ), mStartTrans( sead::Vector3f::zero ), mFallFrames( 60 ), _70( false )
{
}
#endif

#ifdef NON_MATCHING
// instruction swap
void FallMapParts::init( const ActorInitInfo& info )
{
        initActorPoseTQSV( this );
        initMapPartsActor( this, info ); // this should be a thunk
        mStartTrans = getTrans( this );
        tryGetArg0( &mFallFrames, getPlacementInfo( info ) );
        initNerve( this, &NrvFallMapParts::Wait );
        initStageSwitchAppear( this, info );
        trySyncStageSwitchAppear( this );
}
#endif

bool FallMapParts::receiveMsg( u32 msg, HitSensor* other, HitSensor* me )
{
        if ( isMsg52( msg ) )
        {
                setNerve( this, &NrvFallMapParts::End );
                return true;
        }
        if ( isMsgPlayerFloorTouch( msg ) && isNerve( this, &NrvFallMapParts::Wait ) )
        {
                setNerve( this, &NrvFallMapParts::FallSign );
                invalidateClipping( this );
                return true;
        }
        return false;
}

#ifdef NON_MATCHING
// inline nop
void FallMapParts::exeAppear()
{
        if ( isFirstStep( this ) )
        {
                validateCollisionPartsBySystem( this );
                if ( !tryStartAction( this, "Appear" ) )
                        goto end; // ?
        }
        if ( isActionEnd( this ) )
        end:
                setNerve( this, &NrvFallMapParts::Wait );
}
#endif

void FallMapParts::exeWait()
{
        if ( isFirstStep( this ) )
        {
                tryStartAction( this, "Wait" );
                validateClipping( this );
        }
}

#ifdef NON_MATCHING
void FallMapParts::exeFallSign()
{
}
#endif

extern "C" bool fn_00268df8( IUseAudioKeeper*,
        const sead::SafeString& name ); // something with sound

#ifdef NON_MATCHING
// inline nop, string locations
void FallMapParts::exeFall()
{
        if ( isFirstStep( this ) )
        {
                tryStartAction( this, "Fall" );
                fn_00268df8( this, "FallStart" );
                setTrans( this, mStartTrans );
        }
        addVelocityToGravity( this, 1.0 );
        scaleVelocity( this, 0.9 );
        if ( isGreaterStep( this, mFallFrames ) )
                setNerve( this, &NrvFallMapParts::End );
}
#endif

void FallMapParts::exeEnd()
{
        if ( isFirstStep( this ) )
        {
                tryStartAction( this, "End" );
                hideModel( this );
                invalidateCollisionPartsBySystem( this );
                setVelocityZero( this );
        }
        if ( isGreaterStep( this, 60 ) )
        {
                setTrans( this, mStartTrans );
                resetPosition( this );
                showModel( this );
                setNerve( this, &NrvFallMapParts::Appear );
        }
}

} // namespace al
```


