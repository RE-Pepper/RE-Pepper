

# File NoteObj.cpp

[**File List**](files.md) **>** [**Game**](dir_c33286056d2acf479cd8641ef845fec1.md) **>** [**src**](dir_d858f423bf5825f9a3db826b6a54a3cc.md) **>** [**MapObj**](dir_9fb1f6495822aa302d379b21d455a7ad.md) **>** [**NoteObj.cpp**](_note_obj_8cpp.md)

[Go to the documentation of this file](_note_obj_8cpp.md)


```C++
#include "MapObj/NoteObj.h"

#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alActorPoseKeeper.h>
#include <LiveActor/alLiveActorFunction.h>
#include <Placement/alPlacementFunction.h>
#include <Scene/alSceneObjHolder.h>

#include "MapObj/CoinRotater.h"

#ifdef NON_MATCHING
// sead inline
NoteObj::NoteObj( const char* name )
    : MapObjActor( name ), mStartQuat( sead::Quatf::unit ), _70( false ), _71( true ), _74( -1 ),
      _78( sead::Vector3f::zero ), mGenerator( nullptr )
{
        rp::createCoinRotater();
}

NoteObj::NoteObj( NoteObjGenerator* generator )
    : MapObjActor( "音符オブジェ" ), mStartQuat( sead::Quatf::unit ), _70( false ), _71( true ), _74( -1 ),
      _78( sead::Vector3f::zero ), mGenerator( generator )
{
        rp::createCoinRotater();
}
#endif

extern "C" void fn_00270fc4( al::LiveActor*, float, int ); // MtxConnector (?)

static const char* sNoteObjArchive = "NoteObj";

#ifdef NON_MATCHING
void NoteObj::init( const al::ActorInitInfo& info ) // STUPID sead inlines
{
        if ( al::isPlaced( info ) )
        {
                al::initActorWithArchiveName( this, info, sNoteObjArchive );
                mStartQuat = al::getQuat( this );
                fn_00270fc4( this, 70.0, 1 );
                _78 = al::getTrans( this );
                al::invalidateClipping( this );
        }
        al::initActorWithArchiveNameNoPlacementInfo( this, info, sNoteObjArchive );
        makeActorDead();
}
#endif

void NoteObj::initAfterPlacement()
{
}

#ifdef NON_MATCHING
// creates new path instead of conditional instructions
void NoteObj::control()
{
        if ( !_71 )
                al::addVelocityToGravity( this, 0.5 );
        al::rotateQuatYDirDegree( this, mStartQuat, rp::getCoinRotateY() );
}
#endif
```


