from utils.utils import *
from utils.display import *


'''
This file defines the functions needed for displaying experimental results. 
'''


def plot_synthetic_img(cmplx_img, img_title, ref_img, display_win=None, display=False, save_dir=None):
    """ Function to plot reconstruction results in recon experiment on synthetic data. """
    # save_fname = None if (save_dir is None) else save_dir + 'recon_cmplx_img'
    # plot_cmplx_img(cmplx_img, img_title=img_title, ref_img=ref_img,
    #                display_win=display_win, display=display, save_fname=save_fname,
    #                fig_sz=[8, 3], mag_vmax=1, mag_vmin=0.5, phase_vmax=0, phase_vmin=-np.pi/4,
    #                real_vmax=1.1, real_vmin=0.8, imag_vmax=0, imag_vmin=-0.6)
      
    # initialize window and determine area for showing and comparing images
    if display_win is None:
        display_win = np.ones_like(revy_obj, dtype=np.complex64)
    non_zero_idx = np.nonzero(display_win)
    blk_idx = [np.amin(non_zero_idx[0]), np.amax(non_zero_idx[0])+1, np.amin(non_zero_idx[1]), np.amax(non_zero_idx[1])+1]
    cmplx_img_rgn = cmplx_img[blk_idx[0]:blk_idx[1], blk_idx[2]:blk_idx[3]]
    
    if ref_img is not None:
        ref_img_rgn = ref_img[blk_idx[0]:blk_idx[1], blk_idx[2]:blk_idx[3]]
    # phase normalization
    cmplx_img_rgn = phase_norm(cmplx_img_rgn, ref_img_rgn)

    mag = plt.imshow(np.abs(cmplx_img_rgn), cmap='gray', vmax=1, vmin=0.9)
    plt.colorbar()
    plt.axis('off')
    plt.savefig(save_dir + '{}_mag'.format(img_title), transparent=True, bbox_inches='tight', pad_inches=0, dpi=160)
    plt.show()
    plt.clf()
   
    phase = plt.imshow(np.angle(cmplx_img_rgn), cmap='gray', vmax=0, vmin=-0.8)
    plt.colorbar()
    plt.axis('off')
    plt.savefig(save_dir + '{}_phase'.format(img_title), transparent=True, bbox_inches='tight', pad_inches=0, dpi=160)
    plt.show()
    plt.clf()

    # amplitude of difference between complex reconstruction and ground truth image
    mag_err = plt.imshow(np.abs(cmplx_img_rgn - ref_img_rgn), cmap='gray', vmax=0.2, vmin=0)
    plt.colorbar()
    plt.axis('off')
    plt.savefig(save_dir + '{}_mag_err'.format(img_title), transparent=True, bbox_inches='tight', pad_inches=0, dpi=160)
    plt.show()
    plt.clf()

    # phase difference between complex reconstruction and ground truth image
    ang_err = pha_err(cmplx_img_rgn, ref_img_rgn)
    phase_err = plt.imshow(ang_err, cmap='gray', vmax=0.4, vmin=-0.4)
    plt.colorbar()
    plt.axis('off')
    plt.savefig(save_dir + '{}_phase_err'.format(img_title), transparent=True, bbox_inches='tight', pad_inches=0, dpi=160)
    plt.show()
    plt.clf()