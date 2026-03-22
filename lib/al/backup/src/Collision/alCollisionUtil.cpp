#include <Collision/alCollider.h>
#include <Collision/alCollisionUtil.h>
#include <LiveActor/alLiveActor.h>

namespace al
{

bool isCollidedGround( const LiveActor* actor )
{
        return actor->getCollider()->getGroundDistance() >= 0;
}

} // namespace al
