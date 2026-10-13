#include "Player/PlayerActor.h"

#include "Player/Player.h"
#include "Player/PlayerProperty.h"

PlayerProperty* PlayerActor::getProperty()
{
        return mPlayer->getProperty();
}
