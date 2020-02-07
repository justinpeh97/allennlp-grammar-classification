// This component is used for all internal and external anchor links.
// External links are determined by the existence of `http` in the URL.

import React from 'react';
import styled from 'styled-components';
import { CubeIcon, RocketIcon, StackIcon, ToolsIcon, TextIcon } from './inlineSVG';

export const IconBox = ({ className, icon, color }) => {
    const getIcon = (icon) => {
        if (icon === 'stack') {
            return <StackIcon />;
        } else if (icon === 'rocket') {
            return <RocketIcon />;
        } else if (icon === 'cube') {
            return <CubeIcon />;
        } else if (icon === 'tools') {
            return <ToolsIcon />;
        } else { // 'default'
            return <TextIcon />;
        }
    }

    return (
        <StyledIconBox className={className} color={color}>
            <OuterWrapper>
                <InnerWrapper>
                    {getIcon(icon)}
                </InnerWrapper>
            </OuterWrapper>
        </StyledIconBox>
    );
};

// Colored square that contains part icon
const StyledIconBox = styled(({ color, ...props }) => <div {...props} />)`
    width: ${({ theme }) => theme.spacing.xxl.getRemValue() * 4}rem;
    background: linear-gradient(151.76deg, ${({ color }) => {
        if (color === 'aqua') {
            return '#1EC2CC 17.77%, #0191A7';
        } else if (color === 'orange') {
            return '#FFC72E 17.77%, #FF9100';
        } else if (color === 'purple') {
            return '#D864C8 17.77%, #A44397';
        } else if (color === 'blue') {
            return '#00C1E8 17.77%, #0278A7';
        } else { // 'default'
            return '#a3b0be 17.77%, #79899c';
        }
    }} 95.72%);
`;

const OuterWrapper = styled.div`
    position: relative;
    width: 100%;
    padding-bottom: 100%;
    height: 0;
`;

const InnerWrapper = styled.div`
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;

    svg {
        width: 56.25%;
        height: 56.25%;
        fill: #fff;
    }
`;
