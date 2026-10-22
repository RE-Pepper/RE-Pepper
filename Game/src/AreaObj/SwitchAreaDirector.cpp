#include <AreaObj/SwitchAreaDirector.h>
#include <AreaObj/SwitchOnAreaGroup.h>
#include <AreaObj/alSwitchKeepOnAreaGroup.h>

#include "Player/PlayerFunction.h" // GAME

SwitchAreaDirector::SwitchAreaDirector()
    : al::LiveActor( "スイッチエリアディレクター" ), mSwitchOnAreaGroup( nullptr ),
      mSwitchKeepOnAreaGroup( nullptr )
{
}

#ifdef NON_MATCHING

// not using stm for vector copy
void SwitchAreaDirector::movement()
{
        sead::Vector3f pos = rp::getPlayerPos();
        if ( mSwitchOnAreaGroup )
                mSwitchOnAreaGroup->update( pos );
        if ( mSwitchKeepOnAreaGroup )
                mSwitchKeepOnAreaGroup->update( pos );
}
#endif
