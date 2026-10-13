#pragma once

#include <Nerve/alNerveExecutor.h>

namespace al
{
class LayoutInitInfo;
}
class GameDataHolder;

class SaveDataAccessSequence : public al::NerveExecutor
{
private:
        // ...
public:
        SaveDataAccessSequence( GameDataHolder* holder, const al::LayoutInitInfo& info );
};
