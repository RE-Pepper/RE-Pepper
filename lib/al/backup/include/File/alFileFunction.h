#pragma once

#include <prim/seadSafeString.h>

namespace al
{

bool isExistArchive( const sead::SafeString& archive );
void loadArchive( const sead::SafeString& archive );

void makeLocalizedArchivePath( sead::BufferedSafeString* out, const sead::SafeString& archive );
void makeStageDataArchivePath( sead::BufferedSafeString* out, const char* stageName, int scenario, const char* type /* Design, Map, Sound */ );

} // namespace al
