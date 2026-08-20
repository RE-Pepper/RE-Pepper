#pragma once

#include <Placement/alPlacementInfo.h>

namespace al
{

class AreaInitInfo
{
private:
        PlacementInfo mPlacementInfo;
        // ?
public:
        PlacementInfo& getPlacementInfo()
        {
                return mPlacementInfo;
        }
};

} // namespace al
