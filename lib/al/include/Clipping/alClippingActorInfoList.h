#pragma once

#include <container/seadPtrArray.h>

namespace al
{

class ClippingActorInfo;

class ClippingActorInfoList
{
private:
        sead::PtrArray<ClippingActorInfo> mInfos;

public:
        ClippingActorInfoList( int );
};

} // namespace al
