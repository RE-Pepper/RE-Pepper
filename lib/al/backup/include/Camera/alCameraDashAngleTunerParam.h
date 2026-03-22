#pragma once

namespace al
{

class ByamlIter;

class CameraDashAngleTunerParam
{
private:
        float mAddAngleMax;
        float mZoomOutOffsetMax;

public:
        CameraDashAngleTunerParam();

        void init( const ByamlIter* ticket );
};

} // namespace al
