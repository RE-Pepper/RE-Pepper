#pragma once

#include <Nerve/alNerveExecutor.h>

namespace al
{
class AudioKeeper;
class LayoutInitInfo;
} // namespace al
class GameCountUp;

class CoinCharger : public al::NerveExecutor
{
private:
        GameCountUp*     mGameCountUp;
        void*            _C;
        void*            _10;
        al::AudioKeeper* mAudioKeeper;

public:
        CoinCharger( const al::LayoutInitInfo& info );
};
