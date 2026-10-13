#pragma once

namespace al
{
class LayoutInitInfo;
class WipeSimpleTopBottom;
} // namespace al

class StageWipeKeeper
{
private:
        al::WipeSimpleTopBottom* mWipes[ 7 ];
        void*                    unk;

public:
        bool isAnyWipeCloseEnd() const;

public:
        StageWipeKeeper( const al::LayoutInitInfo& info );
};
