#include "MapObj/CoinRotator.h"

#include <Scene/alSceneObjHolder.h>

#include "Scene/SceneObjFactory.h"

#ifdef NON_MATCHING
// need to find out what all the space at 0x68 is used for
CoinRotator::CoinRotator()
    : LiveActor( "コイン回転管理" )
{
}

#endif

const char* CoinRotator::getSceneObjName() const
{
        return "コインローテーター";
}

static void fn_00277de0( al::LiveActor*, const al::ActorInitInfo& )
{
}

void CoinRotator::initAfterPlacementSceneObj( const al::ActorInitInfo& info )
{
        fn_00277de0( this, info );
        makeActorAppeared();
}

namespace rp
{

void createCoinRotator()
{
        al::createSceneObj( SceneObj_CoinRotator );
}

float getCoinRotateY()
{
        CoinRotator* rotater = static_cast<CoinRotator*>( al::getSceneObj( SceneObj_CoinRotator ) );
        return rotater->getRotateY();
}

} // namespace rp
