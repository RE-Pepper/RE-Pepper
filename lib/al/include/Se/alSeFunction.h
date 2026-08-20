#pragma once

#include <prim/seadSafeString.h>

namespace al
{
class IUseAudioKeeper;

void startSe( IUseAudioKeeper* p, const sead::SafeString& name );
bool tryStartSe( IUseAudioKeeper* p, const sead::SafeString& name, int /* ? */ );

} // namespace al
