#include <LiveActor/alLiveActor.h>
#include <LiveActor/alLiveActorFlag.h>

namespace al
{

LiveActorFlag::LiveActorFlag()
    : isDead( true ), isClipped( false ), isInvalidClipping( true ), isDrawClipping( false ), flag5( false ),
      isHideModel( false ), isOffCollide( true ), flag8( false ), isValidMaterialCode( false )
{
}

} // namespace al
