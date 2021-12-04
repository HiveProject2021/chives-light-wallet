import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import ChivesIcon from './images/chives.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={ChivesIcon} viewBox="0 0 150 58" {...props} />;
}
