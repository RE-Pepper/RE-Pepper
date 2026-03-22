#include "Player/PlayerActorInitInfo.h"

#include "Player/PlayerInitFunc.h"

PlayerActorInitInfo::PlayerActorInitInfo()
    : mModelInfo( PlayerInitFunc::getModelInfo() ), mAnimInfo( PlayerInitFunc::getAnimInfo() ),
      _8( PlayerInitFunc::fn_00260620() )
{
}
