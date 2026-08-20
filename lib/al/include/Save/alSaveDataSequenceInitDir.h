#pragma once

#include <Save/alSaveDataSequenceBase.h>

namespace al
{

class SaveDataSequenceInitDir : public SaveDataSequenceBase
{
public:
        SaveDataSequenceInitDir();

        virtual void threadFunc( const char* );
};

} // namespace al
